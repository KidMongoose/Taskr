
from flask_sqlalchemy import SQLAlchemy
from models import *
import uuid
from werkzeug.security import generate_password_hash


contacts = [
    {
      "name" : "Gabby Fernandez",
      "telephone" : "9095152222",
      "email" : "gabbyf@test.net",
      "image" : "jorge-salvador---sGwXMAIQU-unsplash.png",
      "company" : "n/a",
      "category" : "friends",
      "contact_type" : "personal",
      "title" : "n/a",
      "notes" : "My side chick",
    },
    {
      "name" : "Chandler Smith",
      "telephone" : "3522346789",
      "email" : "csmith@ex.net",
      "image" : "brooke-cagle-R0Ea06wC2IM-unsplash.png",
      "company" : "Creatives At Work Inc",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Photographer",
      "notes" : "Contact him to find out his rate.",
    },
    {
      "name" : "Zoe Chan",
      "telephone" : "7274563245",
      "email" : "zc@ex.net",
      "image" : "vin-stratton-PKhwAM0LUW8-unsplash.png",
      "company" : "We Heart Design",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Graphic Designer",
      "notes" : "Pay Zoe next week",
    },
    {
      "name" : "Bridget Brooke",
      "telephone" : "2137658900",
      "email" : "bbisonfire@t.net",
      "image" : "bridget.png",
      "company" : "n/a",
      "category" : "friends",
      "contact_type" : "personal",
      "title" : "n/a",
      "notes" : "Plan dinner with the crew.",
    },
    {
      "name" : "Omar Gonzalez",
      "telephone" : "9512347689",
      "email" : "ogomar@example.net",
      "image" : "harps-joseph-tAvpDE7fXgY-unsplash.png",
      "company" : "n/a",
      "category" : "friends",
      "contact_type" : "personal",
      "title" : "n/a",
      "notes" : "n/a",
    },
    {
      "name" : "Khalid George",
      "telephone" : "8187657890",
      "email" : "kggeorge@ex.net",
      "image" : "asso-myron-3nZy59lC_v0-unsplash.png",
      "company" : "Market Wise",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Digital Marketer",
      "notes" : "Ask for quote",
    },
        {
      "name" : "Anna Jones",
      "telephone" : "76098765463",
      "email" : "anna@t.net",
      "image" : "edward-cisneros-_H6wpor9mjs-unsplash.png",
      "company" : "Next Level",
      "category" : "work",
      "contact_type" : "business",
      "title" : "CEO/partner",
      "notes" : "1/12/21 - Talk to her about shipment cost.",
    },
        {
      "name" : "Jonas White",
      "telephone" : "9095256789",
      "email" : "jonas@t.net",
      "image" : "lucas-sankey-9R-CH7PR150-unsplash.png",
      "company" : "n/a",
      "category" : "family",
      "contact_type" : "personal",
      "title" : "n/a",
      "notes" : "n/a",
    },
        {
      "name" : "Ming Cheong",
      "telephone" : "2135678765",
      "email" : "mc@t.net",
      "image" : "jason-hartono-2kgXVT__OPY-unsplash.png",
      "company" : "Ming Cheong Illustrates",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Illustrator",
      "notes" : "Artwork available 1/15, follow up on the 1/5",
    },
        {
      "name" : "Todd Thompson",
      "telephone" : "8134536789",
      "email" : "thompson@t.net",
      "image" : "foto-sushi-6anudmpILw4-unsplash.png",
      "company" : "Art & Sushi",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Art Director",
      "notes" : "n/a",
    },
        {
      "name" : "Johanna Schwartzmann",
      "telephone" : "3134567654",
      "email" : "jschwartzmann@ex.net",
      "image" : "eyoel-kahssay-sc1IFKQA5pU-unsplash.png",
      "company" : "Opal",
      "category" : "work",
      "contact_type" : "business",
      "title" : "Model",
      "notes" : "n/a",
    },
]

users = [
  {
    "name" : "Rocky Latchman",
    "email" : "rlatchman@ex.net",
    "password" : generate_password_hash('Falc0n_90762as'),
    "image" : "default.png",
    "uuid" : uuid.uuid4().hex
   },
   {
    "name" : "Tommy Gaines",
    "email" : "tommy@ex.net",
    "password" : generate_password_hash('AFca656789gvb_'),
    "image" : "default.png",
    "uuid" : uuid.uuid4().hex
   },
    {
    "name" : "Angel Hernandez",
    "email" : "ahernandez@ex.net",
    "password" : generate_password_hash('aZteca012gd87a'),
    "image" : "default.png",
    "uuid" : uuid.uuid4().hex
   }
] 

tasks = [
  {
     "title" : "Take out the trash",
     "priority" : "low",
     "status" : "pending",
     "item_type" : "personal",
     "category" : "chores",
     "task_note" : "Trash man runs on Thursdays at the new place.",
     "user_id" : 2
  },
    {
     "title" : "Call mom",
     "priority" : "high",
     "status" : "pending",
     "item_type" : "personal",
     "category" : "engagement",
     "task_note" : "Order cake for Mothers Day.",
     "user_id" : 1
  },
    {
     "title" : "Order groceries",
     "priority" : "high",
     "status" : "in progress",
     "item_type" : "personal",
     "category" : "necessities",
     "task_note" : "contact food delivery service",
     "user_id" : 3
  },
    {
     "title" : "Contact Thomas Atkins",
     "priority" : "moderate",
     "status" : "complete",
     "item_type" : "business",
     "category" : "contractor",
     "task_note" : "We need find out the status of the signage for the business",
     "user_id" : 3
  },
    {
     "title" : "Pay Electric Bill",
     "priority" : "high",
     "status" : "complete",
     "item_type" : "business",
     "category" : "company",
     "task_note" : "Pay company electric bill",
     "user_id" : 1
  },
    {
     "title" : "Organize office space",
     "priority" : "high",
     "status" : "pending",
     "item_type" : "personal",
     "category" : "chores",
     "task_note" : "n/a",
     "user_id" : 2
  }
]


db.engine.execute(Task.__table__.insert(), tasks)




