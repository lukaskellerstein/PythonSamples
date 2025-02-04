import asyncio
import nats

async def main():
    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    nc = await nats.connect("nats://localhost:4222")

    # Publish messages
    await nc.publish("help", b'Hello')
    await nc.publish("help", b'World')
    await nc.publish("help", b'!!!!!')


    await nc.publish("tenantId.userId.chatId.assistant", b'HIHIHIHIHIHIHIH')
    await nc.publish("tenantId.userId.chatId.user_proxy", b'HAHAHAHAHAHAHAHA')

    # Terminate connection to NATS.
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(main())