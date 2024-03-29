project = { 
  'committee': ["Stella", "Salma", "Kai"],
  'title': "Very Important Project",
  'due_date': "December 14, 2019",
  'id': "3284",
  'steps': [
    {'description': "conduct interviews",
     'due_date': "August 1, 2018"
    },
    {'description': "code of conduct",
     'due_date': "January 1, 2018"
    },
    {'description': "compile results",
     'due_date': "November 10, 2018"
    },
    {'description': "version 1",
     'due_date': "January 15, 2019"
    },
    {'description': "revisions",
     'due_date': "March 30, 2019"
    },
    {'description': "version 2",
     'due_date': "July 12, 2019"
    },
    {'description': "final edit",
     'due_date': "October 1, 2019"
    },
    {'description': "final version",
     'due_date': "November 20, 2019"
    },
    {'description': "Wrap up",
     'due_date': "December 1, 2019"
    }
  ]
}

steps = project['steps']
people = project['committee']

for step in steps: 
  index = steps.index(step) 
  if index in range(0,3):
    step['person'] = 'Stella'
  elif index in range(3,6):
    step['person'] = 'Salma'
  elif index in range(6, 10):
    step['person'] = 'Kai'

print(steps)