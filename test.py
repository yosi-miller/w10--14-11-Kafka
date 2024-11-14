from database.PostgreSQL.postgresql_repository import insert_danger_email

e = {
"email": "jeremy37@example.org",
"username": "jonesalejandra",
"ip_address": "215.67.111.124",
"created_at": "2024-10-15T05:29:13.450066",

"location": {
"latitude": 8.5478895,
"longitude": -135.24204,
"city": "Port Josephburgh",
"country": "PA"
},

"device_info": {
"browser": "Mozilla/5.0",
"os": "iOS",
"device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
},

"sentences": [
"Public quickly spend hear sing.",
"Difference nothing environmental shake decide.",
"Natural southern what nice."
]
}

r  = insert_danger_email(e)
print(r)