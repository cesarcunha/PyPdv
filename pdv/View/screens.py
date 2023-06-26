# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from pdv.Model.login_screen import LoginScreenModel
from pdv.Controller.login_screen import LoginScreenController
from pdv.Model.sale_screen import SaleScreenModel
from pdv.Controller.sale_screen import SaleScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "sale screen": {
        "model": SaleScreenModel,
        "controller": SaleScreenController,
    },
}