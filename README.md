Hobby Code
----------

The repository contains a POC setup of fastAPI with Celery queue and Redis broker. It provides a server that takes a JSON of armies and calculates the winner of battle between the armies.

The armies are specified according to the schema below:
<details>
<summary>Army schema</summary>
{
  "$defs": {
    "Human": {
      "additionalProperties": false,
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "strength": {
          "title": "Strength",
          "type": "integer"
        },
        "life": {
          "title": "Life",
          "type": "integer"
        }
      },
      "required": [
        "name",
        "strength",
        "life"
      ],
      "title": "Human",
      "type": "object"
    },
    "Orc": {
      "additionalProperties": false,
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "strength": {
          "title": "Strength",
          "type": "integer"
        },
        "life": {
          "title": "Life",
          "type": "integer"
        },
        "shout": {
          "title": "Shout",
          "type": "string"
        },
        "repetition": {
          "title": "Repetition",
          "type": "integer"
        }
      },
      "required": [
        "name",
        "strength",
        "life",
        "shout",
        "repetition"
      ],
      "title": "Orc",
      "type": "object"
    },
    "Troll": {
      "additionalProperties": false,
      "properties": {
        "name": {
          "title": "Name",
          "type": "string"
        },
        "strength": {
          "title": "Strength",
          "type": "integer"
        },
        "life": {
          "title": "Life",
          "type": "integer"
        },
        "majestic_roar": {
          "title": "Majestic Roar",
          "type": "string"
        }
      },
      "required": [
        "name",
        "strength",
        "life",
        "majestic_roar"
      ],
      "title": "Troll",
      "type": "object"
    }
  },
  "description": "Collection of monsters with a leader",
  "properties": {
    "members": {
      "items": {
        "anyOf": [
          {
            "$ref": "#/$defs/Troll"
          },
          {
            "$ref": "#/$defs/Orc"
          },
          {
            "$ref": "#/$defs/Human"
          }
        ]
      },
      "title": "Members",
      "type": "array"
    }
  },
  "required": [
    "members"
  ],
  "title": "Army",
  "type": "object"
}
</details>
There are some examples of jsons with army specifications in the examples/ directory.

# Usage
To use the API, you can use curl with one of the examples:
```
curl -H "Content-Type: application/json" --data @examples/two_armies.json https://finitesets.com:8000/
{"task_id":"a95a3b8c-cfd5-4fdd-b27e-958d25409e1e"}
```
You can then query the state of the task e.g.:
```
curl https://finitesets.com:8000/tasks/a95a3b8c-cfd5-4fdd-b27e-958d25409e1e
{"task_id":"15856895-4f5f-4021-8b54-aabaa2d66b33","task_status":"SUCCESS","task_result":"Tumpo's army has won. Ho Ho"}
```
