or f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isdir(path): #if f is a folder search folder and subfolders for filename
            result = find_file(target, path)
            if result is not None:
                return result
            continue
        if f == target:
            filepaths.append(path)
            return filepaths
            
            
    class STOMPFILE:

    def __init__(self, filepath, title, date, time)
            self.filepath = filepath
            self.title = title
            self.date = date
            self.time = time