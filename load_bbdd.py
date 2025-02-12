from app.extensions import db
from run import app
from app.models import Producto


def cargar_datos():

    productos = [
        # Set MATERO
        Producto(nombre="Set matero canasta ecocuero negro", precio=58000, image_url="https://bodelo.com.ar/wp-content/uploads/2022/11/Catalogo-Bodelo-2024-Full-18.jpg", id_categoria=1),
        Producto(nombre="Set matero naranja", precio=57000, image_url="https://blaqueriakasa.com/wp-content/uploads/2021/01/Mochi-naranja-600x659.jpg", id_categoria=1),
        Producto(nombre="Bolso matero negro", precio=61000, image_url="https://acdn.mitiendanube.com/stores/001/050/261/products/img-20230728-wa00711-5ae6cdb1d590abc40516916832112915-640-0.jpg", id_categoria=1),
        Producto(nombre="Set matero personalizado", precio=62000, image_url="https://acdn.mitiendanube.com/stores/001/419/681/products/set-matero-completo-rosa-i-love11-2edf605db9de81009e16316605330053-1024-1024.jpg", id_categoria=1),

        # MATE
        Producto(nombre="Mate de calabaza", precio=17000, image_url="https://t4.ftcdn.net/jpg/05/47/30/07/240_F_547300760_LIrhGX0i9hrtSSV8BiiwIqzfc29WDyND.jpg", id_categoria=2),
        Producto(nombre="Mate de calabaza rústico", precio=15000, image_url="https://as2.ftcdn.net/v2/jpg/05/45/80/81/1000_F_545808163_GDHMhuHlT5ftIhoiSYNXIJ5KB6VtojHn.jpg", id_categoria=2),
        Producto(nombre="Mate de cuero", precio=11000, image_url="https://as2.ftcdn.net/v2/jpg/06/72/47/71/1000_F_672477120_VNyIVYrmIqSexcZyfCQQZ2pLbhQSEB3Z.webp", id_categoria=2),
        Producto(nombre="Mate cimarrón", precio=20000, image_url="https://as2.ftcdn.net/v2/jpg/05/77/11/17/1000_F_577111781_wlCT5rH0U8grwjPLruM0EazeyzYADglH.jpg", id_categoria=2),
        Producto(nombre="Mate camionero", precio=19000, image_url="https://tiendachemate.com.ar/wp-content/uploads/2023/06/Mate-camionero-Nacional-1.jpg", id_categoria=2),
        Producto(nombre="Mate camionero de algarrobo", precio=22000, image_url="https://d22fxaf9t8d39k.cloudfront.net/d603edac27369f369e27c3b5bd110a96698e2213af42d1aa302ab43dea1d30ee57701.jpg", id_categoria=2),
        Producto(nombre="Mate uruguayo con guarda", precio=26000, image_url="https://dcdn.mitiendanube.com/stores/001/666/155/products/m71-97ebabd6c436a6277216246266983673-1024-1024.jpg", id_categoria=2),
        Producto(nombre="Mate uruguayo imperial de calabaza", precio=25000, image_url="https://dcdn.mitiendanube.com/stores/001/716/742/products/mate-negro-c-guarda-e0c3414001a7f5cf7b17236494454539-240-0.jpg", id_categoria=2),
        Producto(nombre="Mate de algarrobo imperial", precio=22000, image_url="https://d22fxaf9t8d39k.cloudfront.net/575a273408b7e56c2eb2b759db20ac25bb68a39be7142d4a18ce85fa19537bee57701.jpg", id_categoria=2),
        Producto(nombre="Mate de acero negro", precio=14000, image_url="https://www.nakaoutdoors.com.ar/img/articulos/2022/12/waterdog_mate_termico_acero_inoxidable_imagen1.jpg", id_categoria=2),
        Producto(nombre="Mate Stanley verde", precio=25000, image_url="https://www.capitanyo.com.ar/13998-home_default/mate-stanley-236ml-verde.jpg", id_categoria=2),
        Producto(nombre="Mate torpedo negro", precio=19000, image_url="https://acdn.mitiendanube.com/stores/001/775/110/products/157608039_171558987966089_5200625864195267572_n1-7cce1ab61aaf9bde3516258575098760-1024-1024.jpg", id_categoria=2),

        # BOMBILLA
        Producto(nombre="Bombilla cilíndrica desarmable", precio=8000, image_url="https://dcdn.mitiendanube.com/stores/012/510/products/bombillaaceropicodelorocilindro1-4dd9895c36e7177bde16657591981763-640-0.jpg", id_categoria=3),
        Producto(nombre="Bombilla de acero inoxidable", precio=11000, image_url="https://acdn.mitiendanube.com/stores/003/859/300/products/whatsapp-image-2023-12-05-at-13-37-24-1-1d0b05c5bbf89b576a17017953041116-1024-1024.jpg", id_categoria=3),
        Producto(nombre="Bombilla de acero con limpiador", precio=10000, image_url="https://acdn.mitiendanube.com/stores/929/820/products/20368cr-606d67e24d1d579b6e17127040929244-1024-1024.jpg", id_categoria=3),
        Producto(nombre="Bombilla plana", precio=12000, image_url="https://clickandfoods.com/cdn/shop/products/D_NQ_NP_731362-MLA32615791456_102019-O_480x480.jpg", id_categoria=3),
        Producto(nombre="Bombilla Rosamonte", precio=9000, image_url="https://acdn.mitiendanube.com/stores/805/409/products/bombilla-cucharita1-ee011450d4dba6be3116708713144163-640-0.jpg", id_categoria=3),

        # TERMO
        Producto(nombre="Termo de acero", precio=30000, image_url="https://acdn.mitiendanube.com/stores/001/085/687/products/mate-justo-23-f1a58e4f333ece3d0f17001422633188-1024-1024.jpg", id_categoria=4),
        Producto(nombre="Termo Stanley negro", precio=50000, image_url="https://www.perozzi.com.ar/35793-large_default/stanley-termo-mate-system-classic-800-10-10296-001-negro.jpg", id_categoria=4),
        Producto(nombre="Termo Sakura blanco", precio=45000, image_url="https://dominodeco.com.ar/wp-content/uploads/2022/04/termo-sakura.jpg", id_categoria=4),
        Producto(nombre="Termo Sakura verde", precio=43000, image_url="https://acdn.mitiendanube.com/stores/929/820/products/termo-sakura-clasico-de-acero-inoxidable-1l-verde-11-9789e3ca1dad5f9c2416792579894101-1024-1024.jpg", id_categoria=4),
        Producto(nombre="Termo Discovery rosa", precio=39000, image_url="https://mall.icbc.com.ar/36884900-large_default/termo-mate-1-3-litros-discovery-acero-inoxidable-color-rosa.jpg", id_categoria=4)
    ]


    db.session.bulk_save_objects(productos)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        cargar_datos()
