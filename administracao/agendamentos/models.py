from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q


class Agendamento(models.Model):
	STATUS_CHOICES = [
		('P', 'Pendente'),
		('A', 'Aprovado'),
		('R', 'Reprovado'),
	]

	usuario = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='agendamentos'
	)
	sala = models.ForeignKey(
		'salas.Sala',
		on_delete=models.PROTECT,
		related_name='agendamentos'
	)
	data = models.DateField()
	horario_inicio = models.TimeField()
	horario_fim = models.TimeField()
	motivo = models.TextField(blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
	justificativa_reprovacao = models.TextField(blank=True, null=True)
	criado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-data', 'horario_inicio']
		verbose_name = 'Agendamento'
		verbose_name_plural = 'Agendamentos'

	def __str__(self):
		return f"#{self.pk} - {self.sala} em {self.data} ({self.horario_inicio}–{self.horario_fim})"

	def clean(self):
		# validações básicas
		super().clean()

		if self.horario_inicio >= self.horario_fim:
			raise ValidationError({'horario_inicio': 'Horário de início deve ser anterior ao horário de fim.'})

		# Verifica conflitos com agendamentos APROVADOS existentes na mesma sala e data
		if self.sala and self.data and self.horario_inicio and self.horario_fim:
			conflicts = Agendamento.objects.filter(
				sala=self.sala,
				data=self.data,
				status='A'  # apenas agendamentos aprovados bloqueiam
			).exclude(pk=self.pk).filter(
				~(
					Q(horario_fim__lte=self.horario_inicio) |
					Q(horario_inicio__gte=self.horario_fim)
				)
			)

			if conflicts.exists():
				raise ValidationError('Conflito de horário: já existe um agendamento aprovado nesta sala nesse intervalo.')

	def save(self, *args, **kwargs):
		# garante que a validação seja executada sempre que salvar
		self.full_clean()
		return super().save(*args, **kwargs)

