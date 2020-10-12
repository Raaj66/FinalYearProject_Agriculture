import smtplib
import email.message
import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')
import datetime
email_content = """\
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

   <title>Location Based Crop suggested Report</title>
   <style type="text/css">
   
   </style>
</head>

<body>


<table width="100%" cellpadding="0" cellspacing="0" bgcolor="grey"><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p><a href="#">View in Browser</a></p>
      </td>
    </tr>
  </table>

<table id="main" width="600" align="center" cellpadding="0" cellspacing="15"  bgcolor="ffffff">
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" background="" bgcolor="8fb3e9">
          <tr>
            <td width="570" align="center"  bgcolor="grey"><h1>Data Reporting</h1></td>
          </tr>
          <tr>
            <td width="570" align="right" bgcolor="lightgreen"><p>{0}</p></td>
          </tr>
        </table>
      </td>
    </tr>

    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>
              <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
              <img src="https://lucidgreen.io/wp-content/uploads/gettyimages-1135398660-170667a__FocusFillWzExNzAsNjU4LCJ5Iiw2MF0.jpg" width="350" height="250"  />
            </td>
              <td width="15"></td>
            <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://technostacks.com/wp-content/uploads/2018/10/machine-learning-farming-robot.jpg" width ="350" height="250" />
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table id="content-4" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td width="200" valign="top">
              <h5>Insights about Location</h5>
              <p></p>
            </td>
            <td width="15"></td>
            <td width="200" valign="top">
              <h5>Insight about cop</h5>
              <p></p>
            </td>
          </tr>
        </table>
      </td>
    </tr>


  </table>
  <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p>{0} Design better experiences for web & mobile</p>
        <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
      </td>
    </tr>
  </table><!-- top message -->
</td></tr></table><!-- wrapper -->

</body>
</html>


""".format(datetime.date.today())

msg = email.message.Message()
msg['Subject'] = 'A.I generated Report'

msg['From'] = 'internsangular@gmail.com'
msg['To'] = 'harishjrao@gmail.com'
password = "internship123"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

# Login Credentials for sending the mail
s.login(msg['From'], password)

s.sendmail(msg['From'], [msg['To']], msg.as_string())

server = smtplib.SMTP('smtp.gmail.com:587')

