FROM postgres:alpine3.20

# 環境変数を設定（必要に応じて変更してください）
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# ポート5432を公開
EXPOSE 5432

# コンテナのエントリーポイント（デフォルトのまま）
CMD ["postgres"]

# コンテナ起動時に実行するコマンド（デフォルトのまま）
ENTRYPOINT ["docker-entrypoint.sh"]