import json

for idx, fpath in enumerate(['/tmp/video1.json', '/tmp/video2.json'], 1):
    print(f'=== VIDEO {idx} ===')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('Title:', data.get('title'))
    print('Uploader:', data.get('uploader'))
    print('Description:\n', data.get('description'))
    chapters = data.get('chapters')
    if chapters:
        print('Chapters:')
        for c in chapters:
            print(f"  {c.get('start_time')}s: {c.get('title')}")
    else:
        print('No chapters')
    print('='*50)

