import { Button, Checkbox, Form, Input } from "antd";
const onFinish = (values) => {
  console.log("Success:", values);
};
const onFinishFailed = (errorInfo) => {
  console.log("Failed:", errorInfo);
};

const Home = () => {
  return (
    <div className="flex justify-center items-center h-[90vh]">
      <Form
        className="shadow-lg py-10 rounded-md w-full mx-auto max-w-xl"
        name="basic"
        labelCol={{
          span: 8,
        }}
        wrapperCol={{
          span: 12,
        }}
        initialValues={{
          remember: false,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="on"
      >
        <Form.Item
          label="Login"
          name="username"
          rules={[
            {
              required: true,
              message: "Iltimos Loginingni kiriting!",
            },
          ]}
        >
          <Input
            style={{
              padding: 6,
            }}
            className="focus:border-[#6e00c2] hover:border-[#6e00c2]"
          />
        </Form.Item>

        <Form.Item
          label="Parol"
          name="password"
          rules={[
            {
              required: true,
              message: "Iltimos Parolingizni kiriting!",
            },
          ]}
        >
          <Input.Password
            style={{
              padding: 6,
            }}
            className="focus:border-[#6e00c2] hover:border-[#6e00c2]"
          />
        </Form.Item>

        <Form.Item
          name="remember"
          valuePropName="checked"
          wrapperCol={{
            offset: 8,
            span: 10,
          }}
        >
          <Checkbox>Meni eslab qol!</Checkbox>
        </Form.Item>

        <Form.Item
          wrapperCol={{
            offset: 8,
            span: 10,
          }}
        >
          <Button type="primary" htmlType="submit" className="bg-[#6e00c2]">
            Login
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Home;
