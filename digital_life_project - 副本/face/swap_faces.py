import insightface
import numpy as np
from insightface.app import FaceAnalysis


class FaceSwapper:
    def __init__(self):
        self.face_analyzer = FaceAnalysis(name='buffalo_l')
        self.face_analyzer.prepare(ctx_id=0, det_size=(640, 640))
        self.face_swapper_model = insightface.model_zoo.get_model('inswapper_128.onnx', download=True, download_zip=True)

    def swap_faces(self, source_img, target_img, swap_face_no):
        source_img = np.array(source_img)
        target_img = np.array(target_img)
        swap_face_no = int(swap_face_no)

        source_faces = self.face_analyzer.get(source_img)
        source_faces = sorted(source_faces, key=lambda x: x.bbox[0])
        assert len(source_faces) == 1
        source_face = source_faces[0]

        target_faces = self.face_analyzer.get(target_img)
        target_faces = sorted(target_faces, key=lambda x: x.bbox[0])

        target_img = self.face_swapper_model.get(target_img, target_faces[swap_face_no - 1], source_face, paste_back=True)

        return target_img