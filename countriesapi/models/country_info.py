# -*- coding: utf-8 -*-

"""
    countriesapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CountryInfo(object):

    """Implementation of the 'countryInfo' model.

    This model lets user to store country name and code

    Attributes:
        code (string): This indicates the code of country
        value (string): This indicates the name of country

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "value":'value'
    }

    def __init__(self,
                 code=None,
                 value=None):
        """Constructor for the CountryInfo class"""

        # Initialize members of the class
        self.code = code
        self.value = value


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        code = dictionary.get('code')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(code,
                   value)


