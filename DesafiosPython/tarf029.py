print('='*60)
vel = int(input('O veiculo se movia a quantos kms por hora?:'))
if vel >=81:
    multa = float(7 * (vel - 80))
    print('O veiculo esta {}km/kms acima do limite de velocidade'.format(vel - 80))
    print('Portanto o condutor será multado no valor de {:.2f}R$'.format(multa))
else:
    print('O veiculo respeita as normas de trânsito.')
print('='*60)

