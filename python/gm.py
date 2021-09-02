import json
from algorithms.inversion import execute_inversion


class GMModel():
    '''
    Gravity/Magnetics Model
    ---
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialize Gravity Modeling
        '''
        self.project_name = ""
        self.ambient_field = 0.0
        self.inclination = 0.0
        self.units = ""
        self.azimuth = 0.0
        self.modeling_mode = ""
        self.project_file = kwargs["project_file"]
        self.new_project = kwargs["new_project"]

        if self.new_project:
            # Take all the parameters and create a new save file
            # Check what modeling we want
            if self.modeling_mode == "gravity":
                # Do gravity modeling
                pass
            elif self.modeling_mode == "magnetics":
                # Do a magnetics model
                pass
        else:
            # Grab the configurations from the json file
            f = open(self.project_file, mode="r")
            configuration = json.load(f)

            self.project_name = configuration["project_name"]
            self.ambient_field = configuration["ambient_field"]
            self.inclination = configuration["inclination"]
            self.units = configuration["units"]
            self.azimuth = configuration["azimuth"]
            self.modeling_mode = configuration["modeling_mode"]

    def inversion(self, *args, **kwargs):
        '''
        Inversion Program
        '''
        execute_inversion(ambient_field=self.ambient_field)
