# Konnect-API
### A Restful API for Konnect


**User Management Endpoints:**
- *(GET)* /user/list
- *(GET PATCH DELETE)* /user/details/<slug:username>/
- *(POST)* /user/register/

**Authentication Endpoints**
- *(POST)* /oauth/token/
- *(POST)* /oauth/revoke_token/
- *(POST)* /oauth/introspect/
