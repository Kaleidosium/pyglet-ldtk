from ldtk.pyglet_ldtk_loader import Ldtk

def test_fields():
    print("Loading Entities.ldtk...")
    # We need to point to the file
    loader = Ldtk("tests/samples/Entities.ldtk")
    level = loader.levels[0]
    
    print(f"Level loaded: {level.identifier}")
    
    # Find an Enemy entity
    enemies = level.GetEntitiesByID("Enemy")
    if not enemies:
        print("No Enemy found!")
        return

    enemy = enemies[0]
    print(f"Found Enemy at {enemy.x}, {enemy.y}")
    
    # Inspect fields
    # Currently, Entity doesn't have 'props', so we check data['fieldInstances']
    fields = enemy.data.get("fieldInstances", [])
    print("Raw Field Instances:")
    for f in fields:
        print(f"  {f['__identifier']}: {f['__value']} (Type: {f['__type']})")

    # Check if props exists (it shouldn't yet)
    if hasattr(enemy, "props"):
        print("\nEntity has 'props' attribute:")
        print(enemy.props)
    else:
        print("\nEntity does NOT have 'props' attribute yet.")

if __name__ == "__main__":
    test_fields()
