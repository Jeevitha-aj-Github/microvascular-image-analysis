% Estimate optical flow (pseudocode)
flow = opticalFlowFarneback(frame1, frame2);

% Compute magnitude map from flow vectors
[magnitude, angle] = cart2pol(flow(:,:,1), flow(:,:,2));

% magnitude = speed of motion
% angle = direction of motion
