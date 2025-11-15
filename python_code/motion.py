import cv2

def optical_flow(frame1, frame2):
    """
    Expect uint8 grayscale frames.
    Returns dense optical flow field.
    """
    flow = cv2.calcOpticalFlowFarneback(
        frame1, frame2, None,
        0.5,   # pyr_scale
        3,     # levels
        15,    # winsize
        3,     # iterations
        5,     # poly_n
        1.2,   # poly_sigma
        0,     # flags
    )
    return flow
