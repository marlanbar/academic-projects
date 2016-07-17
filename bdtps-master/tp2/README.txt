No se como poner Monto o EsRubi. En nuestra base de datos pusimos que los pagos sean un atributo multivaluado, pero no se si eso se puede controlar a mano. 

Me parece mas prudente si unicamente vigilamos si el usuario pago el mes actual, e imaginamos que no se pueden pagar fuera de orden. Es decir, si pagaste el ultimo mes es por que pagaste todos los meses desde la inscripcion.

En Abono si o si tenemos que sacar fecha, por que ese dato nos juega en contra. De hecho, yo directamente sacaria eso de la factura, por que en nuestra tabla no tenemos forma de recuperarlo. (aun si pudieramos pagar mes por mes, no podriamos saber en que mes lo pagamos)

Las calificaciones solo pueden ser sobre las ventas, ya que en nuestra base de datos de ejemplo no incluimos la posibilidad de darle feedback al comprador.

Por ultimo, a publicacion le puse el ID del servicio y del articulo en vez de aclarar el tipo. Si el servicio es null, entonces es un articulo. Si el articulo es null, entonces es servicio. Si ninguno es null, es mixto.


