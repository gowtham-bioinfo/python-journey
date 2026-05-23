# Day 4  : 30 Days of python programming  , start = 10:48 | End = 12:47 am

# xercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.

# Iterate 10 to 0 using for loop, do the same using while loop.

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

# Use for loop to iterate from 0 to 100 and print only even numbers

# Use for loop to iterate from 0 to 100 and print only odd numbers

# Exercises: Level 2


# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world





# empty list
empty = []
empty = ["Book","Pen","Notes","Chair","Mobile"]
print(len(empty))

first = empty[0]
second = empty[2]
third = empty[-1]
print(first,second,third)

mixed_data_types =["Dileep,20, 5'3 , Not Married,India"]
it_companies =["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(mixed_data_types,it_companies)
print(len(it_companies))

first = it_companies[0]
second = it_companies[3]
third = it_companies[-1]
print(first,second,third)

it_companies.append("GWEN")
it_companies.insert(1, "AWS")
it_companies[1] = it_companies[1].upper()
it_companies[-1] = it_companies[-1].lower()
it_companies = " # " . join(it_companies)
result = "Facebook" in it_companies
print(result)

it_companies =["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.reverse()
print(it_companies)

it_companie=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

it_companies.reverse()
first3 =it_companies[:3]
print(first3)
last3 = it_companies[-3:]
print(last3)
middle = it_companies[3]
print(middle)
first = it_companies[0]
print(first)
last = it_companies[-1]
print(last)
all = it_companies[::7]
print(all)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
result = front_end + back_end
print(result)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,"Python")
print(full_stack)
full_stack.insert(6,"SQL")
print(full_stack)



#Exercise 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
print(ages)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.sort()
i = (len(ages))


if i % 2 == 0 :
    median = (ages[i//2-1] + ages[i//2]) /2
else :
    median = ages[i//2]   
print(median)    

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
average = sum(ages) / len(ages)
print(average)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.sort
age_range = ages[-1] - ages[0]
print(age_range)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
average = sum(ages) / len(ages)
dif_min = abs(min_age-average)
dif_max = abs(max_age-average)
print("abs(min_age-average ", dif_min)
print("abs(max_age-average)", dif_max)


countries = countries = [
'Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cabo Verde',
'Cambodia',
'Cameroon',
'Canada',
'Central African Republic',
'Chad',
'Chile',
'China',
'Colombia',
'Comoros',
'Congo, Democratic Republic of the',
'Congo, Republic of the',
'Costa Rica',
"Côte d'Ivoire",
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'East Timor (Timor-Leste)',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Eswatini',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea, North',
'Korea, South',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'North Macedonia',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Palestine',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent and the Grenadines',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Sudan',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Sweden',
'Switzerland',
'Syria',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe'
]

i = len(countries)
if i % 2 == 0 :
    middle = countries[i//2-1 : i//2+1]

else :
    middle = countries[i//2]    

print(f"Middle Country : {middle}")   

co = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third,*scandiac_countries= co
print("First", first)
print("Second", second)
print("Third", third)
print("Scandic Countries",scandiac_countries)


