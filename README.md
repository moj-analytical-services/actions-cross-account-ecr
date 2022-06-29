# actions-cross-account-ecr

This Action builds ensures that all images published to 
the data engineering repo will be accessable by MWAA in the data account.
The provided account ID and role should be that of the data engineering ECR 
account, and will be inherited from the template unless specified.

## Usage

### Basic

```yaml
steps:
  - name: Add cross-account permissions to an image on ECR
    uses: moj-analytical-services/add-ecr-permissions@v1
    with:
      role-to-assume: arn:aws:iam::123456789012:role/my-role
      account-id: 345678901234
```

It is recommended to set `role-to-assume` and `account-id` using a secret.

## License

The scripts and documentation in this project are released under the
[MIT License](./LICENSE).
