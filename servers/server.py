from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

# Create an MCP server
mcp = FastMCP(
        "Weather Service",
        stateless_http=True,
    )

# Tool implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location."""
    return f"Weather in {location}: Sunny, 72°F"


# Resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 72°F"


# Prompt implementation
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""

# Genera la aplicación Starlette/ASGI base
fastmcp_asgi_app = mcp.streamable_http_app()

# Configura el CORSMiddleware
cors_middleware = CORSMiddleware(
    app=fastmcp_asgi_app, # Envuelve la aplicación generada por mcp
    allow_origins=["*"], # Permite cualquier origen. Cambia '*' por una lista de tus dominios en producción.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# La aplicación final a ejecutar es el middleware envolviendo la app base
app_with_cors = cors_middleware


# Run the server
if __name__ == "__main__":
    import uvicorn
    # Ejecuta la aplicación envuelta con el middleware
    uvicorn.run(app_with_cors, host="127.0.0.1", port=8000)
