<!--Category:C#,SQL--> 
 <p align="right">
    <a href="http://productivitytools.tech/productivitytools-createsqlserverdatabase/"><img src="Images/Header/ProductivityTools_green_40px_2.png" /><a> 
    <a href="https://www.github.com/pwujczyk/ProductivityTools.CreateSQLServerDatabase"><img src="Images/Header/Github_border_40px.png" /></a>
</p>
<p align="center">
    <a href="http://http://productivitytools.tech/">
        <img src="Images/Header/LogoTitle_green_500px.png" />
    </a>
</p>

# GCP.SecretManager

This is a simple python app which returns

- Hello under http://127.0.0.1:8080/Hello
- Secret under http://127.0.0.1:8080/Secret


```
gcloud app create --project banded-edge-363320
gcloud app deploy
```
## Tutorial
[Link](https://cloud.google.com/secret-manager/docs/create-secret)

![](Images/2022-09-22-22-17-28.png)

```
echo -n "pwValue" | gcloud secrets versions add pwsecret --data-file=-
gcloud secrets list
```