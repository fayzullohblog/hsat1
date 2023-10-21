import { Button, Checkbox, Form, Input } from "antd";

const onFinish = (values) => {
  console.log("Success:", values);
};

const onFinishFailed = (errorInfo) => {
  console.log("Failed:", errorInfo);
};

const Home = () => {
  return (
    <div className="flex justify-center items-center flex-col h-[90vh] ">
      <img src="icons/HSAT_logo.png" alt="HSAT logo" className="w-24 h-24" />
      <h3 className="font-bold text-lg text-center leading-4 mb-6">
        Toshkent shahar statistika <br /> boshqarmasi HSAT
      </h3>
      <Form
        className="bg-white rounded-[14px] border p-24 shadow-md flex flex-col"
        name="basic"
        style={{
          maxWidth: 800,
        }}
        initialValues={{
          remember: true,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="on"
      >
        <Form.Item
          name="username"
          rules={[
            {
              required: true,
              message: "Iltimos loginni kiriting!",
            },
          ]}
        >
          <Input placeholder="Login" />
        </Form.Item>

        <Form.Item
          name="password"
          rules={[
            {
              required: true,
              message: "Iltimos parolni kiriting!",
            },
          ]}
        >
          <Input.Password placeholder="Parol" />
        </Form.Item>

        <Form.Item name="remember" valuePropName="checked">
          <Checkbox>Meni eslab qol!</Checkbox>
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" className="bg-blue-400">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Home;
