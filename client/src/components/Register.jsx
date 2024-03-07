function Register() {
  return (
    <div class="flex justify-center items-center h-screen bg-gradient-to-r from-violet-200 to-pink-200">
      <div class="w-96 p-6 shadow-lg bg-white rounded-md">
        <h1 class="text-3xl block text-center font-semibold">
          <i class="fa-solid fa-user"></i> Registration
        </h1>
        <div class="mt-3">
          <label for="username" class="block text-base mb-2">
            Username
          </label>
          <input
            type="text"
            id="username"
            class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600"
            placeholder="Enter Username..."
          />
        </div>
        <div class="mt-3">
          <label for="email" class="block text-base mb-2">
            Email
          </label>
          <input
            type="text"
            id="email"
            class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600"
            placeholder="Enter Email..."
          />
        </div>
        <div class="mt-3">
          <label for="password" class="block text-base mb-2">
            Password
          </label>
          <input
            type="password"
            id="password"
            class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600"
            placeholder="Enter Password..."
          />
        </div>
        <div class="mt-3">
          <label for="repeat_password" class="block text-base mb-2">
            Repeat Password
          </label>
          <input
            type="password"
            id="repeat_password"
            class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600"
            placeholder="Repeat Password..."
          />
        </div>
        <div class="mt-5">
          <button
            type="submit"
            class="border-2 border-indigo-700 bg-indigo-700 text-white py-1 w-full rounded-md hover:bg-transparent hover:text-indigo-700 font-semibold"
          >
            <i class="fa-solid fa-right-to-bracket"></i>Sign Up
          </button>
        </div>
        <div class="mt-5 flex justify-center">
          <p className="mr-1">Already have an account? </p>
          <a href="#" class="text-indigo-800 font-semibold">
            Sign in!
          </a>
        </div>
      </div>
    </div>
  )
}

export default Register
