from waapi import WaapiClient
import os

# Function to import audio files using WAAPI
def waapi_import_file(client: WaapiClient, work_unit_name: str, import_actor_mixer: str, container_type: str,
                      container_name: str, sound_type: str, audio_files: list):
    imports = []
    for i, audio_file in enumerate(audio_files, start=1):
        object_path = f"\\Actor-Mixer Hierarchy\\<WorkUnit>{work_unit_name}\\<Actor-Mixer>{import_actor_mixer}\\<{container_type}>{container_name}\\<Sound>{sound_type}_{container_name}_{i:02}"
        audio_file_path = os.path.abspath(audio_file)
        import_data = {
            'audioFile': audio_file_path,
            'objectPath': object_path,

        }
        imports.append(import_data)

    args = {
        "importOperation": "createNew",
        "default": {
            "importLanguage": sound_type
        },
        "imports": imports
    }

    try:
        result = client.call("ak.wwise.core.audio.import", args)
        print("Audio files imported successfully")
        imported_obj_ids = [item["id"] for item in result["objects"]]
        return imported_obj_ids
    except Exception as e:
        print("Error during import:", e)
        return None
