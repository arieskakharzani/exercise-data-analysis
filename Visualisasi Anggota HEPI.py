#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd

df = pd.read_csv ("data_anggota_HEPI.csv", delimiter = ";" )
df


# In[35]:


# VISUALISASI
# Distribusi Usia Anggota HEPI
import matplotlib.pyplot as plt
from datetime import datetime

df['Tanggal lahir'] = pd.to_datetime(df['Tanggal lahir'])
df['Usia'] = datetime.now() - df['Tanggal lahir']
df['Usia'] = df['Usia'].apply(lambda x: x.days // 365)  # Menghitung usia dalam tahun

plt.figure(figsize=(8, 5))
plt.hist(df['Usia'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Distribusi Usia Anggota HEPI')
plt.xlabel('Usia (Tahun)')
plt.ylabel('Jumlah Anggota')
plt.show()


# In[36]:


# Distribusi Pendidikan Terakhir berdasarkan Jenis Kelamin
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Pendidikan terakhir', hue='Jenis kelamin', palette='pastel')
plt.title('Distribusi Pendidikan Terakhir berdasarkan Jenis Kelamin')
plt.xlabel('Tingkat Pendidikan Terakhir')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=45)
plt.legend(title='Jenis Kelamin', loc='upper right')
plt.show()


# In[37]:


# Pekerjaan/Profesi yang Paling Umum
plt.figure(figsize=(10, 6))
df['Profesi/pekerjaan'].value_counts().head(10).plot(kind='bar', color='lightblue')
plt.title('Top 10 Pekerjaan/Profesi yang Paling Umum di HEPI')
plt.xlabel('Pekerjaan/Profesi')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[38]:


# Distribusi Alamat Rumah berdasarkan Provinsi
plt.figure(figsize=(12, 6))
df['Provinsi Rumah'].value_counts().plot(kind='bar', color='salmon')
plt.title('Distribusi Alamat Rumah Anggota HEPI Berdasarkan Provinsi')
plt.xlabel('Provinsi')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[39]:


import seaborn as sns

# Distribusi Pendidikan Terakhir berdasarkan Usia
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Pendidikan terakhir', y='Usia', palette='coolwarm')
plt.title('Hubungan antara Pendidikan Terakhir dan Usia Anggota HEPI')
plt.xlabel('Tingkat Pendidikan Terakhir')
plt.ylabel('Usia (Tahun)')
plt.xticks(rotation=45)
plt.show()


# In[40]:


# Visualisasi Jenis Kelamin
plt.figure(figsize=(8, 5))
df['Jenis kelamin'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribusi Jenis Kelamin Anggota HEPI')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=0)
plt.show()


# In[33]:


# Visualisasi Pendidikan Terakhir
plt.figure(figsize=(8, 5))
df['Pendidikan terakhir'].value_counts().plot(kind='bar', color='lightcoral')
plt.title('Tingkat Pendidikan Terakhir Anggota HEPI')
plt.xlabel('Tingkat Pendidikan Terakhir')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=45)
plt.show()


# In[41]:


# Mengambil 10 top provinsi kantor
top_provinsi_kantor = df['Provinsi Kantor'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
top_provinsi_kantor.plot(kind='bar', color='lightgreen')
plt.yticks([0, 2, 4, 6, 8])
plt.title('Top 10 Provinsi Kantor Anggota HEPI')
plt.xlabel('Provinsi Kantor')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[42]:


import seaborn as sns
import matplotlib.pyplot as plt

laki_laki_df = df[df['Jenis kelamin'] == 'Laki-laki']
provinsi_counts_laki = laki_laki_df['Provinsi Rumah'].value_counts().head(10)
plt.figure(figsize=(12, 6))
provinsi_counts_laki.plot(kind='bar', color='lightblue')
plt.title('Distribusi Provinsi Rumah Anggota Laki-laki HEPI (Top 10)')
plt.xlabel('Provinsi Rumah')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=45)
plt.show()


# In[43]:


import matplotlib.pyplot as plt

provinsi_counts = df['Provinsi Rumah'].value_counts().head(10)
plt.figure(figsize=(10, 6))
provinsi_counts.plot(kind='bar', color='lightblue')
plt.title('Distribusi Provinsi Rumah Anggota HEPI (Top 10)')
plt.xlabel('Provinsi Rumah')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=45)
plt.show()


# In[44]:


import matplotlib.pyplot as plt

bidang_keahlian_counts = df['Bidang keahlian'].value_counts().head(15)
plt.bar(bidang_keahlian_counts.index, bidang_keahlian_counts.values, color='lightgreen')
plt.title('Top 15 Bidang Keahlian Anggota HEPI')
plt.xlabel('Bidang Keahlian')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()



# In[24]:


# Top 10 Provinsi Rumah Anggota HEPI
import matplotlib.pyplot as plt

# Mengambil 10 top provinsi rumah
top_provinsi_kantor = df['Provinsi Rumah'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
top_provinsi_kantor.plot(kind='bar', color='lightgreen')
plt.yticks([0, 2, 4, 6, 8])
plt.title('Top 10 Provinsi Rumah Anggota HEPI')
plt.xlabel('Provinsi Rumah')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[45]:


import seaborn as sns
import matplotlib.pyplot as plt

perempuan_df = df[df['Jenis kelamin'] == 'Perempuan']
provinsi_counts_perempuan = perempuan_df['Provinsi Kantor'].value_counts().head(10)
plt.figure(figsize=(12, 6))
provinsi_counts_perempuan.plot(kind='bar', color='lightgreen')
plt.title('Distribusi Provinsi Kantor Anggota Perempuan HEPI (Top 10)')
plt.xlabel('Provinsi Kantor')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=45)
plt.show()



# In[46]:


import matplotlib.pyplot as plt

laki_laki_df = df[df['Jenis kelamin'] == 'Laki-laki']
pendidikan_counts_laki = laki_laki_df['Pendidikan terakhir'].value_counts()
plt.pie(pendidikan_counts_laki, labels=pendidikan_counts_laki.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink'])
plt.title('Distribusi Pendidikan Terakhir Anggota Laki-laki HEPI')
plt.show()


# In[47]:


import matplotlib.pyplot as plt
perempuan_df = df[df['Jenis kelamin'] == 'Perempuan']
bidang_keahlian_counts_perempuan = perempuan_df['Bidang keahlian'].value_counts().head(5)
plt.pie(bidang_keahlian_counts_perempuan, labels=bidang_keahlian_counts_perempuan.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink'])
plt.title(f'Distribusi Bidang Keahlian Anggota Perempuan HEPI (Top 5)')
plt.show()


# In[48]:


# Distribusi Letak Kantor berdasarkan Provinsi
plt.figure(figsize=(12, 6))
df['Provinsi Kantor'].value_counts().plot(kind='bar', color='salmon')
plt.title('Distribusi Alamat Kantor Anggota HEPI Berdasarkan Provinsi')
plt.xlabel('Kota')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[49]:


import pandas as pd
from datetime import datetime

# Konversi tanggal lahir ke tipe data datetime
tanggal_lahir = pd.to_datetime(df['Tanggal lahir'])

# Hitung usia
tanggal_sekarang = datetime.now()
usia = tanggal_sekarang - tanggal_lahir

# Ambil komponen tahun dari usia
usia_tahun = usia.dt.days // 365

# Tampilkan usia
print(usia_tahun)

# Distribusi Jumlah Usia dari Anggota Hepi
plt.figure(figsize=(12, 6))
usia_tahun.value_counts().plot(kind='bar', color='blue')
plt.title('Distribusi Jumlah Usia dari Anggota Hepi')
plt.xlabel('Usia')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[50]:


import matplotlib.pyplot as plt

# Mengambil 10 top provinsi rumah
top_provinsi_kantor = df['Provinsi Rumah'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
top_provinsi_kantor.plot(kind='bar', color='lightgreen')
plt.yticks([0, 2, 4, 6, 8])
plt.title('Top 10 Provinsi Rumah Anggota HEPI')
plt.xlabel('Provinsi Rumah')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()



# In[52]:


import matplotlib.pyplot as plt

# Mengambil 10 top provinsi kantor
top_provinsi_kantor = df['Provinsi Kantor'].value_counts().nlargest(10)

plt.figure(figsize=(12, 6))
top_provinsi_kantor.plot(kind='bar', color='lightgreen')
plt.yticks([0, 2, 4, 6, 8])
plt.title('Top 10 Provinsi Kantor Anggota HEPI')
plt.xlabel('Provinsi Kantor')
plt.ylabel('Jumlah Anggota')
plt.xticks(rotation=90)
plt.show()


# In[55]:


plt.figure(figsize=(12, 6))
sns.swarmplot(x='Pendidikan terakhir', y='Usia', data=df, palette='Pastel1')
plt.title('Distribusi Usia berdasarkan Pendidikan Terakhir')
plt.xlabel('Pendidikan Terakhir')
plt.ylabel('Usia (Tahun)')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




