function WienerReduc(infile, outfile)
if nargin < 2
   fprintf('Usage: Wiener noisyfile.wav outFile.wav \n\n');
   return;
end
[x,fs] = audioread(infile);
x = x(:, 1);

[out,~] = WienerNoiseReduction(x,fs,1000)

audiowrite(outfile, out,fs);
end
