# 基础镜像：使用官方Python 3.11精简版
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 先拷贝依赖清单并安装（利用Docker层缓存加速构建）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝应用代码
COPY app.py .

# 暴露5000端口
EXPOSE 5000

# 启动命令
CMD ["python", "app.py"]