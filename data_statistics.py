# Import libraries 
import numpy as np
import pandas as pd

# Dictionary of experience codes
experience_codes = {'EN': 'Entry', 'MI': 'Medium', 'SE': 'Senior', 'EX': 'Expert'}

# Dictionary of employment codes
employment_codes ={'PT': 'Part Time', 'FT': 'Full Time'}

# Dictionary of country codes 
country_codes = {
            'AF': 'Afghanistan',
            'AX': 'Aland Islands', 
            'AL': 'Albania', 
            'DZ': 'Algeria', 
            'AS': 'American Samoa', 
            'AD': 'Andorra', 
            'AO': 'Angola', 
            'AI': 'Anguilla', 
            'AQ': 'Antarctica', 
            'AG': 'Antigua and Barbuda', 
            'AR': 'Argentina', 
            'AM': 'Armenia', 
            'AW': 'Aruba', 
            'AU': 'Australia', 
            'AT': 'Austria', 
            'AZ': 'Azerbaijan', 
            'BS': 'Bahamas', 
            'BH': 'Bahrain', 
            'BD': 'Bangladesh', 
            'BB': 'Barbados', 
            'BY': 'Belarus', 
            'BE': 'Belgium', 
            'BZ': 'Belize', 
            'BJ': 'Benin', 
            'BM': 'Bermuda', 
            'BT': 'Bhutan', 
            'BO': 'Bolivia', 
            'BA': 'Bosnia and Herzegovina', 
            'BW': 'Botswana', 
            'BV': 'Bouvet Island', 
            'BR': 'Brazil', 
            'VG': 'British Virgin Islands', 
            'IO': 'British Indian Ocean Territory', 
            'BN': 'Brunei Darussalam', 
            'BG': 'Bulgaria', 
            'BF': 'Burkina Faso', 
            'BI': 'Burundi', 
            'IN': 'India', 
            'US': 'United States'}

# Dictrionary of company size codes
size_codes = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}