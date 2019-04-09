RootPath = '/Volumes/SAMSUNG/Simulaciones';
OutputPath = '/Users/CesarMB13/Google Drive/Conferences/2019/LANET2019/medyfinol/LANET2019/output';

listing = dir(strcat(RootPath,'/*.mat'));

for n=1:length(listing)
    v = listing(n).name(9:end-4);
    K = load(strcat(RootPath,'/',listing(n).name));
    K = K.K;
    K(K<0) = -1;
    K(K>0) = +1;
    net_interaction = sum(K,2);
    
    % Save output
    filename = strcat(OutputPath,'/net_int_v_',v,'.txt');
    dlmwrite(filename, net_interaction, 'precision','%.2f');
end

