from pyodbc import connect

cnxn = connect(r'Driver=SQL Server;Server=LAPTOP-A4542TO0;Database=ngochuong_net;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute(
    """
    SELECT [Post_Title]
      ,[Post_Brief]
      ,[Post_Description]
      ,[Post_FullText]
    FROM [ngochuong_net].[dbo].[wcms_Post]
    """)
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row)
cnxn.close()