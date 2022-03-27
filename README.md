# Vanced-Archive

This repo includes all vanced versions and can be used as a mirror on Vanced Manager.

  

  

## Installing Vanced Manager

Download and install the last version Vanced Manger from [wayback machine](https://web.archive.org/web/20220313225204/https://github.com/YTVanced/VancedManager/releases/latest/download/manager.apk) (wait for a few seconds so it redirects you to download) as manager downloads seem to be removed from their github.

  

  

## Selecting this repo as mirror

(this step may not be required for now because vanced manager seems to fall back to `https://mirror.codebucket.de/vanced/api/v1/` if vanced's own mirror doesn't work) 



After installing manager,

Open settings(Click on three dots at the top right than select settings) > Open dev settings (Click on the gear at the top right) > Click on Channel url

 Replace `https://api.vancedapp.com/api/v1` with `https://raw.githubusercontent.com/kaanyalova/vanced-archive/master/api/v1`

or `https://raw.githubusercontent.com/kaanyalova/vanced-archive/master/api/beta`  if you want to use beta versions of youtube vanced.



Alternatively you can use the [offical mirror](https://www.reddit.com/r/Vanced/wiki/index) as it seems to work for now, to do this replace `https://api.vancedapp.com/api/v1` with `https://mirror.codebucket.de/vanced/api/v1` or `https://mirror.codebucket.de/vanced/api/beta` if you want to use beta versions of youtube vanced.



These mirrors does not include microg as it is downloaded from [Vanced's github](https://github.com/TeamVanced/VancedMicroG/releases/tag/latest/) (downloads still seem to work fine) when using Vanced Manager.



You can also just download and install the apks normally without using Vanced Manager. (either from this repo or from official mirror)

  

  

## Verifying the apks (optional)

Becuse you might not trust some random guy on internet you might want to verify if  the apks are coming from vanced ,to do this you can,

  

### Verifying files with checksums from vanced developers

Vanced developer canelex_ shared sha256 hashes of recent versions of vanced on [reddit](https://www.reddit.com/r/Vanced/comments/tdazfr/discontinuation_of_the_vanced_project/i0isgho/) so you can use

```bash
sha256sum filename.apk
```

and compare the hashes.

  

### Verifying files with signature from vanced's website

[Vanced's website](vancedapp.com) has sha256 signatures so you can verify that the files are coming from them to do that you can use

```bash
keytool -printcert -jarfile filename.apk
```

and compare the `SHA256` with the one in their website

  

  

## Other

I got these files from a torrent file on [Vanced's Discord Server](https://discord.gg/wYrRPgv) it was on vanced_mirrors channel before it was removed. This repo also includes [that torrent file](https://github.com/kaanyalova/vanced-archive/blob/master/Vanced.torrent).

  

This repo also includes the repo for Integrations (Sponsorblock/ReturnDislikes) that was later removed. I got the files from [wayback machine](https://web.archive.org/web/20220313213618/https://github.com/YTVanced/Integrations)










