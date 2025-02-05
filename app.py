from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


app = FastAPI()

data = [
  {
    "name": "John Doe",
    "occupation": "Software Engineer",
    "address": "123 Main St"
  },
  {
    "name": "Jane Smith",
    "occupation": "Data Scientist",
    "address": "456 Elm St"
  },
  {
    "name": "Michael Johnson",
    "occupation": "Web Developer",
    "address": "789 Oak St"
  },
  {
    "name": "Emily Brown",
    "occupation": "UX Designer",
    "address": "101 Maple Ave"
  },
  {
    "name": "David Lee",
    "occupation": "Product Manager",
    "address": "202 Pine St"
  },
  {
    "name": "Sarah Taylor",
    "occupation": "Marketing Specialist",
    "address": "303 Cedar St"
  },
  {
    "name": "Chris Evans",
    "occupation": "Graphic Designer",
    "address": "404 Walnut St"
  },
  {
    "name": "Jessica White",
    "occupation": "Financial Analyst",
    "address": "505 Birch St"
  },
  {
    "name": "Matthew Miller",
    "occupation": "Systems Administrator",
    "address": "606 Spruce St"
  },
  {
    "name": "Amanda Martinez",
    "occupation": "HR Coordinator",
    "address": "707 Chestnut St"
  }
]

class Person(BaseModel): #creates a class with attribute data types
    name: str
    occuption: str
    address: str

@app.get("/name")  #creates a get request for name
async def get_person_name():
    name_list = []  #creates a list to hold names of persons
    for person in data:  # for loop adds every person's name from dictionary to name_list
        name_list.append(person["name"]) #add person name from dictionary to name_list
    return name_list  #returns the list of names

@app.get("/occupation")  #creates a get request for occupation
async def get_person_occuption():
    list_of_occuption = [] #creates a list to hold each person occupation
    for person_occuption in data: #for loop adds everyone's occupation from dictionary to occupation list
        list_of_occuption.append(person_occuption["occupation"])
    return list_of_occuption #returns the list of occupation

@app.get("/address")  #creates a get request for address
async def pet_person_address():
    list_of_address = []
    for addresses in data:  #for loop adds everyone's address from dictionary to address list
        list_of_address.append(addresses["address"])
    return list_of_address #returns the list of addresses