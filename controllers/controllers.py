# -*- coding: utf-8 -*-

# class Empleado-car(http.Controller):
#     @http.route('/empleado-car/empleado-car/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empleado-car/empleado-car/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empleado-car.listing', {
#             'root': '/empleado-car/empleado-car',
#             'objects': http.request.env['empleado-car.empleado-car'].search([]),
#         })

#     @http.route('/empleado-car/empleado-car/objects/<model("empleado-car.empleado-car"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empleado-car.object', {
#             'object': obj
#         })
