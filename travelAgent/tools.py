from google.adk.tools import ToolContext

def set_home_location(location: str, tool_context: ToolContext):
  # Store in USER scope
  tool_context.state["user:home_location"] = location

  # Set persistent instruction
  tool_context.state["user:home_location_instruction"] = f"""
      The customer's home location is: {location}.
      If they do not specify a different starting location, you should 
      add this home location as the first city of the itinerary.
    """
  return f"Home location set to {location}."

def add_city(tool_context: ToolContext, city: str):
  # Get from SESSION scope (defaults to empty list)
  itinerary = tool_context.state.get("itinerary", [])

  itinerary.append(city)

  # Update SESSION scope
  tool_context.state["itinerary"] = itinerary
  return {"status": f"Added {city} to the itinerary."}

def create_itinerary(tool_context: ToolContext):
    """
    Creates the itinerary legs based on the session-scoped itinerary.
    """
    itinerary = tool_context.state.get("itinerary", [])

    home = tool_context.state.get("user:home_location")

    legs = []

    # If itinerary exists but does not specify a starting point
    if itinerary:
        if home and itinerary[0] != home:
            # Prepend home location
            full_list = [home] + itinerary
        else:
            full_list = itinerary
    else:
        # No itinerary — maybe user only has a home location
        if home:
            return {"itinerary": [], "note": "No trip planned yet, but home location is set."}
        return {"itinerary": [], "note": "No trip planned."}

    # Build legs
    for i in range(len(full_list) - 1):
        legs.append({
            "from": full_list[i],
            "to": full_list[i + 1]
        })

    return {"itinerary": legs}