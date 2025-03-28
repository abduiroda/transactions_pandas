import pandas as pd

data = {
    'Дата': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-02-01', '2024-02-10'],
    'Клиент ID': [1001, 1002, 1001, 1003, 1002],
    'Тип операции': ['Пополнение', 'Снятие', 'Пополнение', 'Снятие', 'Пополнение'],
    'Сумма': [5000, 2000, 3000, 1000, 4000]
}

df = pd.DataFrame(data)
df['Дата'] = pd.to_datetime(df['Дата'])

#1. Подсчет общей суммы пополнений и снятий для каждого клиента
total_by_client = df.groupby(['Клиент ID', 'Тип операции'])['Сумма'].sum().unstack(fill_value=0)
print("Общая сумма по клиентам:\n", total_by_client)

#2. Клиент с наибольшей суммой пополнений
top_client = total_by_client['Пополнение'].idxmax()
print(f"\nКлиент с наибольшей суммой пополнений: Клиент {top_client}")

#3. Месяц с наибольшей суммой транзакций
df['Месяц'] = df['Дата'].dt.to_period('M') 
top_month = df.groupby('Месяц')['Сумма'].sum().idxmax()
print(f"\nМесяц с наибольшей суммой транзакций: {top_month}")

total_by_client.plot(kind='bar', stacked=True, color=['green', 'red'])
plt.title('Сумма пополнений и снятий по клиентам')
plt.xlabel('Клиент ID')
plt.ylabel('Сумма (в рублях)')
plt.legend(title='Тип операции')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
