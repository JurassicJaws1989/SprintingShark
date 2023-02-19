import cx_Freeze

executables = [cx_Freeze.Executable("Sprinting Shark Remastered.py")]

cx_Freeze.setup(
    name="Sprinting Shark - Remastered 1.0.0.1",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["crate.png"]}},

    executables = executables


    )
