import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('Titanic-Dataset.csv')

titanic = titanic.drop(columns="Cabin")
#  no of null values in each column

titanic = titanic.fillna(titanic['Age'].mean())
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])


# all null values are filled now
male_servived = titanic[titanic['Sex'] == 'male']['Survived'].sum()
female_servived = titanic[titanic['Sex'] == 'female']['Survived'].sum()
print('male survived :' ,male_servived)
print('female survived :' ,female_servived)
# # print(titanic.isnull().sum())

# gender_by_survived =  titanic.groupby(['Pclass','Sex'])['Survived'].mean().reset_index()
# # print(gender_by_survived)
# male = gender_by_survived[gender_by_survived['Sex'] == 'male']
# female = gender_by_survived[gender_by_survived['Sex'] == 'female']

# plt.plot(male['Pclass'], male['Survived'], marker='o', label='Male')
# plt.plot(female['Pclass'], female['Survived'], marker='o', label='Female')
# plt.title('Suvival Rate by Gender and Pclass')
# plt.xlabel('Pclass')
# plt.ylabel('Survival Rate')
# plt.legend()
# plt.show()


# survived analysis using Embarked
# embark_map = {'C': 1, 'Q': 2, 'S': 3}
# titanic['Embarked_num'] = titanic['Embarked']

# embared_survival = titanic.groupby('Embarked_num')['Survived'].sum()
# # print(embared_survival)
# plt.bar(embared_survival.index.tolist(), embared_survival.values).map(embark_map)
# plt.title('Survival Rate by Embarked Location')
# plt.xlabel('Embarked')
# plt.ylabel('Survival Rate')
# plt.legend(['1 = Cherbourg (C)\n2 = Queenstown (Q)\n3 = Southampton (S)'])
# plt.show()


# survived analysis using fare and survival rate

fare_survival = titanic.groupby('Fare')['Survived'].mean()
plt.scatter(fare_survival.index, fare_survival.values)
plt.title('Survival Rate by Fare')
plt.xlabel('Fare')
plt.ylabel('Survival Rate')
plt.show()
# print(titanic.info())

