% Normalize intensities
img = double(img);
img = (img - min(img(:))) / (max(img(:)) - min(img(:)));

% Denoise using bilateral filter
denoised = imbilatfilt(img);

% Enhance contrast locally
enhanced = adapthisteq(denoised);
