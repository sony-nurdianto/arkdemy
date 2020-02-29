import json

biodata = '''

{
  "nama": "sony nurdianto",
  "age": 22,
  "addres": "kedurus Gg 4a no 32",
  "hobby": [
    "belajar coding",
    "baca komik ",
    "nonton anime"
  ],
  "is_married": false,

  "list_school" :
  [
    {
      "school_name" : "SMK Kartika 2 surabaya",
      "year_in" : 2012,
      "year_out" : 2015,
      "major" : "tehnik kendaraan ringan"
    }
  ],

  "skill" :
  [
    {
      "beginner" : "saya newbie di segala bidang",
      "advanced" : null,
      "expert" : null

    }
  ],
  "interest_in_coding" : true

}
'''

data= json.loads(biodata)
print("nama : " + data['nama'])
print ("umur : " , data['age'])
print ("alamat : " +data['addres'])

for hoby in data['hobby'] :
  print(hoby)

print (data['is_married'])

for list_schhol in data['list_school'] :
  print(list_schhol)

for skills in data ['skill'] :
  print (skills)