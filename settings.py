import data_functions as fc

class Settings():
    """inicaite settings"""
    def __init__(self):
        """iniciate settings"""
        #setting business type needed
        self.business_type = fc.read_files('business_type.txt')

        #columns needed for compute
        self.distribution_column = fc.read_files('distribution_column.txt')

        #setting staff exceptions
        self.staff_exceptions = fc.read_files('staff_exceptions.txt')