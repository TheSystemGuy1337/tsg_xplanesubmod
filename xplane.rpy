# Register the Submod
# CAUTION: In case of compiler error, use bundled fire extinguisher

init -990 python in mas_submod_utils:
    Submod(
        author="TheSystemGuy",
        name="XPlane Reaction Submod",
        description="Submod for allowing Monika to react to the X-Plane flight simulator.",
        version="1.0",
        dependencies={},
        settings_pane=None,
    )

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database, # Register window react in MAS database
            eventlabel="mas_wrs_xp11", # Tie our registered window react to an event label
            category=[": X-Plane|X-System"], # Look for windows with "X-Plane or X-System" in the title bar
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_xp11:
    $ wrs_success = mas_display_notif( # Engage payload, trigger window react system and send notification 
        m_name,
        [
            "Playing with your flight simulator, [player]?",
            "You are clear for takeoff, [player]",
        ],
        'Window Reactions'
    )
    if not wrs_success: # Failure handler
        $ mas_unlockFailedWRS('mas_wrs_xp11') 
    return


