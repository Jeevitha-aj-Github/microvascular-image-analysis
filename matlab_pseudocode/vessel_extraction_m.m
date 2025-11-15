% Thresholding to create vessel mask
t = graythresh(img);
mask = img > t;

% Remove small objects (noise)
mask = bwareaopen(mask, 50);

% Skeletonisation to extract vessel centre-lines
skeleton = bwskel(mask);

% Approximate vessel width by area / skeleton length
width_estimate = sum(mask(:)) / sum(skeleton(:));
