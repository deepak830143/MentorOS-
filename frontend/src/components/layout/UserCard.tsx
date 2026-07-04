interface UserCardProps {
  name: string;
  role: string;
}

export default function UserCard({
  name,
  role,
}: UserCardProps) {
  return (
    <div className="rounded-2xl bg-slate-100 p-4">
      <div className="flex items-center gap-3">
        <div className="flex h-12 w-12 items-center justify-center rounded-full bg-blue-600 text-lg font-bold text-white">
          {name.charAt(0)}
        </div>

        <div>
          <p className="font-semibold text-slate-800">
            {name}
          </p>

          <p className="text-sm text-slate-500">
            {role}
          </p>
        </div>
      </div>
    </div>
  );
}