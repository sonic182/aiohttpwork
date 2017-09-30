"""Sample UserController.

Minimal endpoint for users.
"""

from json import dumps

from app.decorators.json import JsonValidate
from app.controllers.base import Controller
from app.models.user import User

CONSTRAIN = {
    'name': {
        'format': r'^[\w\s]+$'
    }
}


class UserController(Controller):
    """User controller."""

    async def index(self, req):
        """Index test route."""
        req.logger.info('%s: Request por hacer a mongo' % req.uuid)
        data = await User(req.app).find({}).to_list(None)
        data = User.serialize(data)
        req.logger.info('%s: Respuesta mongo: %s' % (req.uuid, dumps(data)))
        return self.json_response(data)

    @JsonValidate(CONSTRAIN)
    async def create(self, req):
        """Do test route."""
        data = req.payload
        user = await User(req.app).insert_one(data)
        data['_id'] = str(user.inserted_id)
        await self.write(req, self.json_response(data))
        print('can continue doing stuff...')
