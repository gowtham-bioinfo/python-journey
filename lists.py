# Day 4  : 30 Days of python programming  , start = 10:48 | End = 12:47 am

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

it_companies =["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

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


# Day 5  : 30 Days of python programming  , start = 6:29 pm | End =  10:53 pm | lists again


empty=[]
empty =["Pen","Book","Notes","Egg","Love"]
print(len(empty))
first = empty[0]
middle = empty[2]
last = empty[-1]
print(first,middle,last)

mixed_data_types = ["Arya","20","5'8","Not Married","ATP"]
it_companies = ["Facebbok","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(mixed_data_types)
print(it_companies)
print(len(it_companies))

first = it_companies[0]
middle = it_companies[3]
last = it_companies[-1]
print(first,middle,last)
it_companies.append("Star Sports")
print(it_companies)
it_companies.insert(0,"Willow")
print(it_companies)

it_companies = ["Facebbok","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies[0]=it_companies[0].upper()
print(it_companies)
result = " # " . join(it_companies)
print(it_companies)
print("Facebook" in it_companies)
print(it_companies.sort)
first3 = it_companies[0:3]
print(first3)
last3 = it_companies[-3:]
it_companies.reverse()
print(it_companies)
first3 = it_companies[3]
last = it_companies[-3:]
middle = it_companies[4]

it_companies = ["Facebbok","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
first = it_companies[1:]
print(first)
it_companies.pop(-1)
print(it_companies)
middle = len(it_companies)//2
it_companies.pop(middle)
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
result = front_end + back_end
print(result)

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, "Python")
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
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
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



# Day 6  : 30 Days of python programming  , start = 7:24 pm| End =  8:53 pm | Exercise 2 Again

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
print(min_age)
print(max_age)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.append(min_age)
print(ages)
ages.append(max_age)
print(ages)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.sort
i = len(ages)

if i % 2 == 0 :
    median = (ages[i//2-1]+ages[i//2])
else :
    median = ages[i//2]   
print(median)    

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
result = sum(ages) / len(ages)
print(result)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
ages.sort
min_age = ages[0]
max_age = ages[-1]
print(min_age)
print(max_age)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 26]
average = sum(ages) / len(ages)
dif_min = abs(min_age-average)
dif_max = abs(max_age-average)
print("abs.min_age-average " ,dif_min)
print("abs.max_age-average" , dif_max)
