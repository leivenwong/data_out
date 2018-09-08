import data_functions as fc

class Settings():
    """inicaite settings"""
    def __init__(self):
        """iniciate settings"""
        self.business_type = fc.read_files('business_type.txt')
        self.distribution_column = fc.read_files('distribution_column.txt')
        self.staff_exceptions = fc.read_files('staff_exceptions.txt')


