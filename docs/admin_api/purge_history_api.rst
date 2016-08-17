Purge History API
=================

The purge history API allows server admins to purge historic events from their
database, reclaiming disk space.

Depending on the amount of history being purged a call to the API may take
several minutes or longer. During this period users will not be able to
paginate further back in the room from the point being purged from.

The API is simply:

``POST /_matrix/client/r0/admin/purge_history/<room_id>/<event_id>``

including an ``access_token`` of a server admin.
