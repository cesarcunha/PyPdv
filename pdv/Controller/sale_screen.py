import importlib

import pdv.View.SaleScreen.sale_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(pdv.View.SaleScreen.sale_screen)


class SaleScreenController:
    """
    The `SaleScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.sale_screen.SaleScreenModel
        self.view = pdv.View.SaleScreen.sale_screen.SaleScreenView(controller=self, model=self.model)

    def get_view(self) -> pdv.View.SaleScreen.sale_screen:
        return self.view
