from models.restaurante import Restaurante

restaurante_sushi_taboao = Restaurante(nome='Sushi Taboão', categoria='Japonesa')
# restaurante_sushi_taboao.receber_avaliacao('Lucas', 6)
# restaurante_sushi_taboao.receber_avaliacao('Amanda', 7)
# restaurante_sushi_taboao.receber_avaliacao('Luis', 2)

restaurante_coco_bambu = Restaurante(nome='Coco Bambu', categoria='Frutos do Mar')
restaurante_pastelaria_cecap = Restaurante(nome='Pastelaria Cecap', categoria='Massas')

restaurante_coco_bambu.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()